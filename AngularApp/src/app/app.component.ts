import { ChangeDetectorRef,ChangeDetectionStrategy, Component,ViewContainerRef } from '@angular/core';
import { RyberService } from './ryber.service';
import { environment as env } from 'src/environments/environment';
import {Route} from '@angular/router';
import { eventDispatcher,numberParse } from './customExports';
import { of,Subscription,fromEvent } from 'rxjs';
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

