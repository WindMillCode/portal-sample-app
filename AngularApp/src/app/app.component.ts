import { ChangeDetectorRef,ChangeDetectionStrategy, Component,ViewContainerRef } from '@angular/core';
import { RyberService } from './ryber.service';
import { environment as env } from 'src/environments/environment';
import {Route} from '@angular/router';
import { eventDispatcher,numberParse,mediaPrefix,RyberProductsItems } from './customExports';
import { of,Subscription,fromEvent,iif } from 'rxjs';
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

