import { Injectable } from '@angular/core';
import { Event, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { iif, of } from 'rxjs';
import { delay,exhaustMap,tap } from 'rxjs/operators';
import { cartCreate, mediaPrefix,RyberStore,RyberProductsItems } from './customExports';
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
            items:[],
            loaded:false
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
                    let [focusout, blur] = Array(2).fill(
                        (evt:Event |any )=>{

                            result.value = evt.target.value
                        }

                    )

                    let result = {
                        placeholder:x,
                        value:  "",
                        focusout,
                        blur
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
                        let [focusout, blur] = Array(2).fill(
                            (evt:Event |any )=>{

                                result.value = evt.target.value
                            }

                        )
                        let result = {
                            placeholder:x,
                            value:  "",
                            focusout,blur
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
                            },
                            focusout:(evt:FocusEvent |any )=>{
                                result.value = evt.target.value
                            },
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
                                },
                                focusout:(evt:FocusEvent |any )=>{
                                    result.value = evt.target.value
                                },
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
                        let myAcctCurrent:any = {
                            user:acctCurrent?.user || "guest",
                            myPass:acctCurrent?.pass,
                            billing:myBilling,
                            shipping:myShipping
                        }
                        console.log(
                            myAcctCurrent,
                            myCartItems,
                            cartTotal.text()
                        )

                        // XHR to backend

                            // get the orderId array


                            // create an order
                            let userOrderIds;
                            http.post(
                                `${env.backend.url}/users/read`,
                                {
                                    data:{
                                        'user':acctCurrent?.user,
                                        'pass':acctCurrent?.pass,
                                        'filter':['orderId']
                                    }
                                }
                            )
                            .pipe(
                                
                                exhaustMap((result:any)=>{
                                    userOrderIds = result.message.data.orderId
                                    return http.put(
                                        `${env.backend.url}/order/create`,
                                        {
                                            data:{
                                                user:acctCurrent?.user || "guest",
                                                cart:myCartItems,
                                                billing:myBilling,
                                                shipping:myShipping,
                                                total:cartTotal.value()
                                            }
                                        }
                                    )
                                }),
                                exhaustMap((result:any)=>{
                                    userOrderIds.push(result.message.orderId)
                                    myAcctCurrent.orderId = userOrderIds
                                    return http.patch(
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
                                }),
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
