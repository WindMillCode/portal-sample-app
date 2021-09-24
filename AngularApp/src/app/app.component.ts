import { Component,ViewContainerRef } from '@angular/core';
import { RyberService } from './ryber.service';
import { environment as env } from 'src/environments/environment';
import {Route} from '@angular/router';
import { eventDispatcher,numberParse } from './customExports';
import { of,Subscription,fromEvent } from 'rxjs';
import { delay,tap,repeat ,concatMap, exhaust, exhaustMap} from 'rxjs/operators';

declare global{
    var Prism:any
}
@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss']
})
export class AppComponent {
    // metadata
    title = 'Portal';
    subs: Subscription[] = [];
    //

    constructor(
        public ryber: RyberService,
        private vcf: ViewContainerRef
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
        let {ryber} = this
        // e2e automation tests you wnat to remove these
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
    }

    ngOnDestroy(): void {
        this.subs
        .forEach((x:any,i)=>{
            x?.unsubscribe();
        })
    }
}

