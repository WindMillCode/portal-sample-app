import { Component, OnInit,ChangeDetectionStrategy,ChangeDetectorRef,HostBinding, HostListener,ViewContainerRef } from '@angular/core';
import {fromEvent,iif,Subscription,of} from 'rxjs';
import { RyberService } from 'src/app/ryber.service';
import { classPrefix,RyberProductsItems,cartCreate } from 'src/app/customExports';
import { environment as env } from 'src/environments/environment';
import {retry, take, tap,delay} from 'rxjs/operators';
import { HttpErrorResponse } from '@angular/common/http';
import {populateProducts} from 'src/app/customExports'

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class MainComponent implements OnInit {

    // metadata
    meta = {
        name:"Shop"
    }
    @HostBinding('class') myClass: string = `a_p_p_${this.meta.name}View`;
    prefix ={
        main:classPrefix( {view:`${this.meta.name}MainPod`}),
        view: classPrefix({view:`${this.meta.name}`}),
        pods:Array(1).fill(null)
        .map((x:any,i)=>{
            return classPrefix({view:`${this.meta.name}Pod`+i})
        })
    }
    subs: Subscription[] = [];
    //

    shop:any={

    }

    constructor(
        private ref: ChangeDetectorRef,
        private vcf:ViewContainerRef,
        public ryber: RyberService
    ) { }

    ngOnInit(): void {
        let {ryber,ref}= this
        // xhr for the products
        if(!ryber.store.products.loaded){
            ryber.store.products.loaded = true
            ryber.http.post(
                `${env.backend.url}/product/list`,
                {}
            )
            .pipe(
                retry(2),
                tap(
                    (result:any)=>{
                        // update the prducts.items
                        ryber.store.products.items = result.message.list
                        .map((x:any,i)=>{
                            let result:RyberProductsItems = {
                                title:{
                                    text:x.title
                                },
                                img:{
                                    src:x.img_url
                                },
                                price:{
                                    text:`$${x.price}`,
                                    value:x.price
                                },
                                addItem:{
                                    click:(evt:MouseEvent)=>{
                                        if(!result.addItem.inCart){
                                            ryber.store.cart.items.push(result)
                                            ryber.router.navigateByUrl('/cart');
                                            result.addItem.inCart = true
                                        }
                                        else{
                                            result.quantity.input.value += 1
                                            ryber.router.navigateByUrl('/cart');
                                        }

                                    // XHR to add item to cart
                                        // there must be user
                                        if(ryber.store.accounts.current.user){
                                            // create or update cart depending on present id
                                            iif(
                                                ()=>{return ryber.store.cart.id === ""},
                                                ryber.http.put(
                                                    `${env.backend.url}/cart/create`,
                                                    {
                                                        cartData:{
                                                            cart:ryber.store.cart.items
                                                            .map((x:any,i)=>{
                                                                return {
                                                                    img:x.img,
                                                                    price:x.price,
                                                                    quantity:{
                                                                        input:x.quantity.input
                                                                    },
                                                                    title:x.title
                                                                }
                                                            }),
                                                            total:ryber.store.cart.total.value(),
                                                        },
                                                        userData:{
                                                            user:ryber.store.accounts.current.user,
                                                            pass:ryber.store.accounts.current.pass
                                                        }
                                                    }
                                                ),
                                                ryber.http.patch(
                                                    `${env.backend.url}/cart/update`,
                                                    {
                                                        data:{
                                                            cart_id:ryber.store.cart.id,
                                                            update_body:{
                                                                cart:ryber.store.cart.items
                                                                .map((x:any,i)=>{
                                                                    return {
                                                                        img:x.img,
                                                                        price:x.price,
                                                                        quantity:{
                                                                            input:x.quantity.input
                                                                        },
                                                                        title:x.title
                                                                    }
                                                                }),
                                                                total:ryber.store.cart.total.value(),
                                                            }
                                                        }
                                                    }
                                                )
                                            )
                                            .pipe(
                                                tap((result:cartCreate |any)=>{
                                                    if(ryber.store.cart.id === ""){
                                                        ryber.store.cart.id = result.message.cartId
                                                    }
                                                },console.error),
                                            )
                                            .subscribe()

                                        }
                                        //
                                    },
                                    inCart:false
                                },
                                removeItem:{
                                    click:(evt:MouseEvent)=>{
                                        let index = ryber.store.cart.items.indexOf(result)
                                        ryber.store.cart.items.splice(index,1)
                                        result.addItem.inCart = false
                                    }
                                },
                                quantity:{
                                    input:{
                                        value:1,
                                        blur:(evt:FocusEvent |any)=>{
                                            result.quantity.input.value = evt.target.value
                                        },
                                        focusout:(evt:FocusEvent |any)=>{
                                            result.quantity.input.value = evt.target.value
                                        }
                                    },
                                    add:{
                                        click:(evt:MouseEvent)=>{
                                            result.quantity.input.value++
                                        }
                                    },
                                    remove:{
                                        click:(evt:MouseEvent)=>{
                                            if(result.quantity.input.value>1){
                                                result.quantity.input.value--
                                            }
                                        }
                                    }
                                },
                                subtotal:{
                                    text:()=>{
                                        return "$"+result.subtotal.value()
                                    },
                                    value:()=>{
                                        let value = (result.price.value*result.quantity.input.value).toFixed(2)
                                        return parseFloat(value)
                                    }
                                }
                            }
                            return result
                        })
                        ref.detectChanges()
                        console.log(ryber.store.products.items)
                        //

                    },
                    (err:HttpErrorResponse)=>{
                        console.log(err)
                        populateProducts({ryber,ref,iif,env,tap})

                    }
                ),
                take(1)
            )
            .subscribe()
        }
        //
    }

    ngOnDestroy(): void {
        this.subs
        .forEach((x:any,i)=>{
            x?.unsubscribe();
        })
    }

}
