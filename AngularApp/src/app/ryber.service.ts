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
            items:["Hot deals","Store","Cart","Checkout"]
            .map((x:any,i)=>{
                return {
                    text:x
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

                            this.store.cart.items.push(result)
                            this.router.navigateByUrl('/cart')
                        }
                    },
                    quantity:{
                        input:{
                            value:1
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
                        text:()=>result.price.value*result.quantity.input.value
                    }
                }
                return result
            })
        },
        cart:{
            empty:true,
            items:Array(1).fill(null)
            .map((x:any,i)=>{
                return {
                    title:{
                        text:"QR Code 1"
                    },
                    img:{
                        src:mediaPrefix({media:'shop_1.png'})
                    },
                    price:{
                        text:"$29.99",
                        value:29.99
                    },
                    quantity:{
                        input:{
                            value:1
                        },
                        add:{
                            click:(evt:MouseEvent)=>{
                                this.store.cart.items[i].quantity.input.value++
                            }
                        },
                        remove:{
                            click:(evt:MouseEvent)=>{
                                if(this.store.cart.items[i].quantity.input.value>1){
                                    this.store.cart.items[i].quantity.input.value--
                                }
                            }
                        }
                    },
                    subtotal:{
                        text:()=>this.store.cart.items[i].price.value*this.store.cart.items[i].quantity.input.value
                    }
                }
            }),
            total:{
                text:()=>this.store.cart.items.reduce((acc,cur)=>{
                    return acc+cur.subtotal.text()
                },0)
            }
        }
    }
}
