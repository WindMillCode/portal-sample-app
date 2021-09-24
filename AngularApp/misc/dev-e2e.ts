// @ts-nocheck

// add sample items to cart
let counter = 0
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

