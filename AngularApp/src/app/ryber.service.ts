import { Injectable } from '@angular/core';
import { Event, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { iif, of } from 'rxjs';
import { delay,tap } from 'rxjs/operators';
import { cartCreate, mediaPrefix,RyberStore } from './customExports';
import { environment as env } from 'src/environments/environment';



@Injectable({
    providedIn: 'root'
})
export class RyberService {

    constructor(
        public router: Router,
        public http: HttpClient
    ) { }

    store:RyberStore = {
        meta:{
            items:["111-222-3333","email@gmail.com","567 ABC Road, Wakanda"]
            .map((x:any,i)=>{
                return {
                    text:x
                }
            })
        },
        categories:{
            items:["Login","Create Account","Store","Cart","Checkout"]
            .map((x:any,i)=>{
                return {
                    text:x,
                    routerLink:["/login","/create-acct","/shop","/cart/","/checkout"][i]
                }
            })
        },
        info:{
            items:["About","Contact","Privacy Policy","Orders/Returns","Terms & Conditions"]
            .map((x:any,i)=>{
                return {
                    text:x
                }
            })
        },
        service:{
            items:["My account","View Cart","Wishlist","Track My Order","Help"]
            .map((x:any,i)=>{
                return {
                    text:x
                }
            })
        },
        products:{
            items:["QR Code 1","QR Code 2","NFT 1", "NFT 2","T-shirt 1","T shirt 2","T -shirt 3"]
            .map((x:any,i)=>{
                let result ={
                    title:{
                        text:x
                    },
                    img:{
                        src:[
                            mediaPrefix({media:'shop_1.png'}),
                            mediaPrefix({media:'shop_1.png'}),
                            mediaPrefix({media:'shop_0.jpg'}),
                            mediaPrefix({media:'shop_0.jpg'}),
                            mediaPrefix({media:'shop_2.jpg'}),
                            mediaPrefix({media:'shop_3.jpg'}),
                            mediaPrefix({media:'shop_4.jpg'}),
                        ][i]
                    },
                    price:{
                        text:["$29.99","$29.99","$54.99","$54.99","$22.99","$25.99","$22.99"][i],
                        value:[29.99,29.99,54.99,54.99,22.99,25.99,22.99][i]
                    },
                    addItem:{
                        click:(evt:MouseEvent)=>{

                            if(!result.addItem.inCart){
                                this.store.cart.items.push(result)
                                this.router.navigateByUrl('/cart');
                                result.addItem.inCart = true
                            }
                            else{
                                result.quantity.input.value += 1
                                this.router.navigateByUrl('/cart');
                            }

                            // XHR to add item to cart
                                // there must be user
                            if(this.store.accounts.current.user){
                                // create or update cart depending on present id
                                iif(
                                    ()=>{return this.store.cart.id === ""},
                                    this.http.put(
                                        `${env.backend.url}/cart/create`,
                                        {
                                            cartData:{
                                                cart:this.store.cart.items
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
                                                total:this.store.cart.total.value(),
                                            },
                                            userData:{
                                                user:this.store.accounts.current.user,
                                                pass:this.store.accounts.current.pass
                                            }
                                        }
                                    ),
                                    this.http.patch(
                                        `${env.backend.url}/cart/update`,
                                        {
                                            data:{
                                                cart_id:this.store.cart.id,
                                                update_body:{
                                                    cart:this.store.cart.items
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
                                                    total:this.store.cart.total.value(),
                                                }
                                            }
                                        }
                                    )
                                )
                                .pipe(
                                    tap((result:cartCreate |any)=>{
                                        if(this.store.cart.id === ""){
                                            this.store.cart.id = result.message.cartId
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
                            let index = this.store.cart.items.indexOf(result)
                            this.store.cart.items.splice(index,1)
                            result.addItem.inCart = false
                        }
                    },
                    quantity:{
                        input:{
                            value:1,
                            blur:(evt:FocusEvent |any)=>{
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
        },
        cart:{
            empty:true,
            items:[],
            total:{
                value:()=>this.store.cart.items.reduce((acc,cur)=>{
                    return acc+cur.subtotal.value()
                },0).toFixed(2),
                text:()=>"$"+this.store.cart.total.value()
            },
            id:""

        },
        accounts:{
            ui:{
                items:["Username","Password"]
                .map((x:any,i)=>{
                    let result = {
                        placeholder:x,
                        value:  "",
                        blur:(evt:Event |any )=>{
                            result.value = evt.target.value
                        }
                    }
                    return result
                })
            },
            logout:{
                click:(evt:MouseEvent)=>{
                    Object.keys(this.store.accounts.current)
                    .forEach((x,i)=>{
                        this.store.accounts.current[x] = ""
                    })
                }
            },
            login:{
                ui:{
                    items:["Username","Password"]
                    .map((x:any,i)=>{
                        let result = {
                            placeholder:x,
                            value:  "",
                            blur:(evt:Event |any )=>{
                                result.value = evt.target.value
                            }
                        }
                        return result
                    })
                },
                submit:{
                    click:(evt:MouseEvent)=>{
                        let user = this.store.accounts.login.ui.items[0].value
                        let pass = this.store.accounts.login.ui.items[1].value
                        let passwords = this.store.accounts.all.items
                        .map((x:any,i)=>{
                            return x.pass
                        })
                        if(passwords.indexOf(pass) !== -1){
                            this.store.accounts.current.user = user
                            this.store.accounts.current.pass = pass
                            this.store.accounts.current.billing = {
                                items:Object.fromEntries(
                                    ["First Name","Last Name","Email","Phone","Address","City","State","Zip Code","Country"]
                                    .map((x:any,i)=>{
                                        return [x.toLowerCase().split(" ").join("_"),""]
                                    })
                                )
                            }
                            this.store.accounts.current. shipping ={
                                info:{
                                    items:Object.fromEntries(
                                        ["First Name","Last Name","Email","Phone","Address","City","State","Zip Code","Country"]
                                        .map((x:any,i)=>{
                                            return [x.toLowerCase().split(" ").join("_"),""]
                                        })
                                    )
                                },
                                sameAsBilling:{
                                    checked:true
                                }
                            }
                        }
                    }
                }
            },
            all:{
                items:[]
        },
            current:{

            }
        },
        checkout:{
            billing:{
                items :Object.fromEntries(
                    ["First Name","Last Name","Email","Phone","Address","City","State","Zip Code","Country"]
                    .map((x:string,i)=>{
                        let result = {
                            placeholder:x,
                            key:x.toLowerCase().split(" ").join("_"),
                            value:  "",
                            blur:(evt:Event |any )=>{
                                result.value = evt.target.value
                            }
                        }
                        return [x,result]
                    })
                )
            },
            shipping:{
                sameAsBilling:{
                    checked:true,
                    change:(evt:Event |any)=>{
                        this.store.checkout.shipping.sameAsBilling.checked = evt.target.checked
                    }
                },
                info:{
                    items:Object.fromEntries(
                        ["First Name","Last Name","Email","Phone","Address","City","State","Zip Code","Country"]
                        .map((x:any,i)=>{
                            let result = {
                                placeholder:x,
                                key:x.toLowerCase().split(" ").join("_"),
                                value:"",
                                blur:(evt:Event |any )=>{
                                    result.value = evt.target.value
                                }
                            }
                            return [x,result]
                        })
                    )
                }
            },
            payment:{
                paypal:{
                    option:{
                        checked:false,
                        change:(evt:Event |any )=>{

                        }
                    }
                },
                placeOrder:{
                    click:(evt:MouseEvent)=>{
                        let {http}= this
                        let acctCurrent = this.store.accounts.current
                        let {billing,shipping} = this.store.checkout
                        let {items:cartItems,total:cartTotal} = this.store.cart

                        let myCartItems = cartItems.map((x:any,i)=>{
                            return {
                                name:x.title.text,
                                price:x.price.value,
                                quantity:x.quantity.input.value
                            }
                        })
                        let myBilling = {
                            items:
                            Object.fromEntries(
                                Object.entries(billing.items)
                                .map(([keyx,valx]:any,i)=>{
                                    return [valx.key,valx.value]
                                })
                            )
                        }
                        let myShipping = {
                            info:{
                                items:shipping.sameAsBilling.checked ? myBilling.items :
                                Object.fromEntries(
                                    Object.entries(shipping.info.items)
                                    .map(([keyx,valx]:any,i)=>{
                                        return [valx.key,valx.value]
                                    })
                                )
                            },
                            sameAsBilling:{
                                checked:shipping.sameAsBilling.checked
                            }
                        }
                        let myAcctCurrent = {
                            user:acctCurrent?.user || "guest",
                            billing:myBilling,
                            shipping:myShipping
                        }
                        console.log(
                            myAcctCurrent,
                            myCartItems,
                            cartTotal.text()
                        )

                        // XHR to backend
                        http.patch(
                            `${env.backend.url}/users/update`,
                            {
                                data:{
                                    user:acctCurrent?.user,
                                    myPass:acctCurrent?.pass,
                                    update_body:myAcctCurrent
                                }
                            }
                        )
                        .pipe(
                            tap(console.log,console.error)
                        )
                        .subscribe()
                        //
                    }
                }
            }
        }
    }
}
