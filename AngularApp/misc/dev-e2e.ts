// @ts-nocheck
// add sample items to cart
of({})
.pipe(
    exhaustMap(()=>{
        let counter = 0
        return of({})
        .pipe(
            delay(500),
            tap(()=>{
                eventDispatcher({
                    element:document.querySelectorAll(".a_p_p_ShopPod0Button0")[Math.floor(Math.random()*6)] as HTMLElement,
                    event:"click"
                })
            }),
            delay(500),
            tap(()=>{
                Array(Math.floor(Math.random()*5)).fill(null)
                .forEach((x:any,i)=>{
                    eventDispatcher({
                        element:document.querySelectorAll(".a_p_p_CartPod0Button1")[counter] as HTMLElement,
                        event:"click"
                    })
                })
                counter++;
            }),
            delay(500),
            tap(()=>{
                ryber.router.navigateByUrl("/shop")
            }),
            repeat(2)
        )
    }),
    delay(3000),
    tap(()=>{
        ryber.router.navigateByUrl("/cart")
    }),
)
.subscribe()
//


// complete auth flow and checkout creating several accounts
of({})
.pipe(
    concatMap(()=>{
        return of({})
        .pipe(
            delay(500),
            tap(()=>{
                ryber.store.accounts.ui.items
                .forEach((x:any,i)=>{
                    x.value = i===0 ?  faker.internet.userName() :
                    faker.internet.password();

                })
                ref.detectChanges()
                eventDispatcher({
                    element:document.querySelectorAll(".a_p_p_CreateAcctPod0Button0")[0] as HTMLElement,
                    event:"click"
                })

            }),
            delay(500),
            tap(()=>{
                ryber.router.navigateByUrl("/create-acct")
            }),
        )
    }),
    exhaustMap(()=>{
        let counter = 0
        return of({})
        .pipe(

            delay(1000),
            tap(()=>{
                ryber.router.navigateByUrl("/shop")
            }),
            delay(500),
            tap(()=>{
                eventDispatcher({
                    element:document.querySelectorAll(".a_p_p_ShopPod0Button0")[Math.floor(Math.random()*6)] as HTMLElement,
                    event:"click"
                })
            }),
            delay(1000),
            tap(()=>{
                Array(Math.floor(Math.random()*5)).fill(null)
                .forEach((x:any,i)=>{

                    try{
                        eventDispatcher({
                            element:document.querySelectorAll(".a_p_p_CartPod0Button1")[counter] as HTMLElement,
                            event:"click"
                        })
                    }
                    catch(e){}
                })
                counter++;
            }),
            delay(500),
            tap(()=>{
                ryber.router.navigateByUrl("/shop")
            }),
            repeat(2)
        )
    }),
    delay(4000),
    tap(()=>{
        ryber.router.navigateByUrl("/checkout")
    }),
    delay(500),
    tap(()=>{
        let {billing,shipping} = ryber.store.checkout
        Object.values(billing.items)
        .forEach((x:any,i)=>{
            x.value = [
                faker.name.firstName(),
                faker.name.lastName(),
                faker.internet.email(),
                faker.phone.phoneNumber(),
                faker.address.streetAddress(),
                faker.address.city(),
                faker.address.state(),
                faker.address.zipCode(),
                faker.address.country()
            ][i]
        })

        // different shipping address
        if([true,false][Math.floor(Math.random()*2)]){

            (document.querySelector(".a_p_p_CheckoutPod0Input1") as HTMLInputElement).click() ;

            Object.values(shipping.info.items)
            .forEach((x:any,i)=>{
                x.value = [
                    faker.name.firstName(),
                    faker.name.lastName(),
                    faker.internet.email(),
                    faker.phone.phoneNumber(),
                    faker.address.streetAddress(),
                    faker.address.city(),
                    faker.address.state(),
                    faker.address.zipCode(),
                    faker.address.country()
                ][i]
            })
        }
        ref.detectChanges();
        //
        eventDispatcher({
            element:document.querySelectorAll(".a_p_p_CheckoutPod0Button0")[0] as HTMLElement,
            event:"click"
        })
    }),
)
.subscribe()
//

// create several  accounts
of({})
.pipe(
    concatMap(()=>{
        return of({})
        .pipe(
            delay(500),
            tap(()=>{
                ryber.store.accounts.ui.items
                .forEach((x:any,i)=>{
                    x.value = i===0 ?  faker.internet.userName() :
                    faker.internet.password();

                })
                ref.detectChanges()
                eventDispatcher({
                    element:document.querySelectorAll(".a_p_p_CreateAcctPod0Button0")[0] as HTMLElement,
                    event:"click"
                })

            }),
            delay(500),
            tap(()=>{
                ryber.router.navigateByUrl("/create-acct")
            }),
            repeat(3)
        )
    })
)
.subscribe()
//


// sample populate ryber.store.products.items
ryber.store.products.items =Array(7).fill(null)
.map((x:string,i)=>{
    let result:RyberProductsItems ={
        title:{
            text:["QR Code 1","QR Code 2","NFT 1", "NFT 2","T-shirt 1","T shirt 2","T -shirt 3"][i]
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
                        tap((result:any |any)=>{
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
//
