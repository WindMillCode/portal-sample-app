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
            repeat(3)
        )
    }),
    exhaustMap(()=>{
        let counter = 0
        return of({})
        .pipe(
            delay(3000),
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
    delay(4000),
    tap(()=>{
        ryber.router.navigateByUrl("/checkout")
    }),
    delay(500),
    tap(()=>{
        let {billing,shipping} = ryber.store.checkout
        billing.items.forEach((x:any,i)=>{
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

            shipping.info.items.forEach((x:any,i)=>{
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
