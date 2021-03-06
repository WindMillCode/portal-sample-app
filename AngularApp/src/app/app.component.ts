import { ChangeDetectorRef,ChangeDetectionStrategy, Component,ViewContainerRef } from '@angular/core';
import { RyberService } from './ryber.service';
import { environment as env } from 'src/environments/environment';
import {Route} from '@angular/router';
import { eventDispatcher,numberParse,mediaPrefix,RyberProductsItems } from './customExports';
import { of,Subscription,fromEvent,iif, Subject } from 'rxjs';
import { delay,tap,repeat ,concatMap, exhaust, exhaustMap} from 'rxjs/operators';
import faker from 'faker';



declare global{
    var Prism:any;
    var faker:any
}
@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss'],
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class AppComponent {
    // metadata
    title = 'Portal';
    subs: Subscription[] = [];
    //

    constructor(
        public ryber: RyberService,
        private vcf: ViewContainerRef,
        private ref:ChangeDetectorRef
    ){}
    ngOnInit() {
        let {ryber,subs} =this;

        //remove version
        if(env.production){
            this.vcf.element.nativeElement.removeAttribute("ng-version");
        }
        //

        // so we dont have to navigate on dev
        if(!env.production){
            ryber.router.navigateByUrl(env.startURL);
        }
        //

    }

    ngAfterViewInit() {
        // dev addtions
        let {ryber,ref} = this
        // e2e automation tests you wnat to remove these

        if(!env.production){
            let mySub = new Subject()

            mySub
            .pipe(
                tap(()=>{
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
                                    // [true,false][Math.random()*2|0] ?  window.location.reload() : null
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
                        delay(3000),
                        tap(()=>{
                            window.location.reload()
                        })
                    )
                    .subscribe()
                })
            )
            .subscribe()
            mySub.next()

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

