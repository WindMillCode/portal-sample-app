import { Component, OnInit,ChangeDetectionStrategy,ChangeDetectorRef,HostBinding, HostListener,ViewContainerRef } from '@angular/core';
import {fromEvent,iif,Subscription,of} from 'rxjs';
import { RyberService } from 'src/app/ryber.service';
import { classPrefix } from 'src/app/customExports';
import { environment as env } from 'src/environments/environment';
import {take, tap} from 'rxjs/operators'



@Component({
    selector: 'app-main',
    templateUrl: './main.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class MainComponent implements OnInit {


    // metadata
    meta = {
        name: "CreateAcct"
    }
    @HostBinding('class') myClass: string = `a_p_p_${this.meta.name}View`;
    prefix = {
        main: classPrefix({ view: `${this.meta.name}Main` }),
        view: classPrefix({ view: `${this.meta.name}` }),
        pods: Array(1).fill(null)
            .map((x: any, i) => {
                return classPrefix({ view: `${this.meta.name}Pod` + i })
            })
    }
    subs: Subscription[] = [];
    //

    accounts = {
        submit:{
            click:(evt:MouseEvent)=>{
                let {ryber,ref}=this
                let newAcct = {
                    user:ryber.store.accounts.ui.items[0].value,
                    pass:ryber.store.accounts.ui.items[1].value,
                    billing:{
                        items:[]
                    },
                    shipping:{
                        info:{
                            items:[]
                        },
                        sameAsBilling:{
                            checked:true
                        }
                    }
                }
                Object.entries(newAcct)
                .forEach((x:any,i)=>{
                    let [keyx,valx] = x
                    ryber.store.accounts.current[keyx]= valx
                })
                ryber.store.accounts.all.items.push(newAcct)
                // XHR to create acct
                ryber.http.put(
                    `${env.backend.url}/users/create`,
                    {
                        data:newAcct
                    }
                )
                .pipe(
                    tap(console.log,console.error),
                    take(1)
                )
                .subscribe()
                //
                console.log(newAcct)
                ryber.router.navigateByUrl("/shop")
                ref.detectChanges()

            }
        },
    }


    constructor(
        private ref: ChangeDetectorRef,
        private vcf: ViewContainerRef,
        public ryber: RyberService
    ) { }

    ngOnInit(): void {

    }

    ngOnDestroy(): void {
        this.subs
        .forEach((x: any, i) => {
            x?.unsubscribe();
        })
    }

}
