import { Component, OnInit,ChangeDetectionStrategy,ChangeDetectorRef,HostBinding, HostListener,ViewContainerRef } from '@angular/core';
import {fromEvent,iif,Subscription,of} from 'rxjs';
import { RyberService } from 'src/app/ryber.service';
import { classPrefix } from 'src/app/customExports';
import { environment as env } from 'src/environments/environment';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class MainComponent implements OnInit {

    // metadata
    meta = {
        name:"Cart"
    }
    @HostBinding('class') myClass: string = `a_p_p_${this.meta.name}View`;
    prefix ={
        main:classPrefix( {view:`${this.meta.name}MainPod`}),
        view: classPrefix({view:`${this.meta.name}`}),
        pods:Array(2).fill(null)
        .map((x:any,i)=>{
            return classPrefix({view:`${this.meta.name}Pod`+i})
        })
    }
    subs: Subscription[] = [];
    //

    cart:any = {
        labels:{
            items:["Image","Title","Price","Quantity","Subtotal"]
            .map((x:any,i)=>{
                return {
                    text:x
                }
            })
        },
        continueShop:{
            click:(evt:MouseEvent)=>{
                this.ryber.router.navigateByUrl('/shop');
            }
        }
    }


    constructor(
        private ref: ChangeDetectorRef,
        private vcf:ViewContainerRef,
        public ryber: RyberService
    ) { }

    ngOnInit(): void {

    }

    ngOnDestroy(): void {
        this.subs
        .forEach((x:any,i)=>{
            x?.unsubscribe();
        })
    }

}
