import { Injectable } from '@angular/core';
import { Event, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { of } from 'rxjs';
import { delay,tap } from 'rxjs/operators';
import { mediaPrefix } from './customExports';


@Injectable({
    providedIn: 'root'
})
export class RyberService {

    constructor(
        public router: Router,
        public http: HttpClient
    ) { }

    store:any = {
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
                    addCart:{
                        click:(evt:MouseEvent)=>{

                            if(!result.addCart.inCart){
                                this.store.cart.items.push(result)
                                this.router.navigateByUrl('/cart');
                                result.addCart.inCart = true
                            }
                            else{
                                result.quantity.input.value += 1
                                this.router.navigateByUrl('/cart');
                            }

                        },
                        inCart:false
                    },
                    removeItem:{
                        click:(evt:MouseEvent)=>{
                            let index = this.store.cart.items.indexOf(result)
                            this.store.cart.items.splice(index,1)
                            result.addCart.inCart = false
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
                                items:[]
                            }
                            this.store.accounts.current. shipping ={
                                info:{
                                    items:[]
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
                items:["First Name","Last Name","Email","Phone","Address","City","State","Zip Code","Country"]
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
            shipping:{
                sameAsBilling:{
                    checked:true,
                    change:(evt:Event |any)=>{
                        this.store.checkout.shipping.sameAsBilling.checked = evt.target.checked
                    }
                },
                info:{
                    items:["First Name","Last Name","Email","Phone","Address","City","State","Zip Code","Country"]
                    .map((x:any,i)=>{
                        let result = {
                            placeholder:x,
                            value:"",
                            blur:(evt:Event |any )=>{
                                result.value = evt.target.value
                            }
                        }
                        return result
                    })
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
                            items:billing.items.map((x:any,i)=>{
                                return {
                                    name:x.placeholder,
                                    value:x.value
                                }
                            })
                        }
                        let myShipping = {
                            items:shipping.sameAsBilling.checked ? myBilling.items :
                            shipping.info.items.map((x:any,i)=>{
                                return {
                                    name:x.placeholder,
                                    value:x.value
                                }
                            }),
                            sameAsBilling:shipping.sameAsBilling.checked
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
                        alert("check console log")
                        //
                    }
                }
            }
        }
    }
}
