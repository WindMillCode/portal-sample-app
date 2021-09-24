import { Component, OnInit,ChangeDetectionStrategy,ChangeDetectorRef,HostBinding, HostListener,ViewContainerRef } from '@angular/core';
import {fromEvent,iif,Subscription,of} from 'rxjs';
import { RyberService } from 'src/app/ryber.service';
import { classPrefix,mediaPrefix } from 'src/app/customExports';
import { environment as env } from 'src/environments/environment';

@Component({
    selector: 'app-main',
    templateUrl: './main.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class MainComponent implements OnInit {

    // metadata
    meta = {
        name: "Home"
    }
    @HostBinding('class') myClass: string = `a_p_p_${this.meta.name}View`;
    prefix = {
        main: classPrefix({ view: `${this.meta.name}MainPod` }),
        view: classPrefix({ view: `${this.meta.name}` }),
        pods: Array(2).fill(null)
            .map((x: any, i) => {
                return classPrefix({ view: `${this.meta.name}Pod` + i })
            })
    }
    subs: Subscription[] = [];
    //

    home = {
        topics:{
            items:["QR Collection","T-Shirt Collection","NFT Collection"]
            .map((x:any,i)=>{
                return {
                    text:x
                }
            })
        },
        products:{
            new:{
                items:["home_0.jpg","home_0.jpg","home_0.jpg"]
                .map((x:any,i)=>{
                    return {
                        img:{
                            src:mediaPrefix({media:x})
                        },
                        title:{
                            text:"New Qrcode style"
                        }


                    }
                })
            }
        }
    }

    constructor(
        private ref: ChangeDetectorRef,
        private vcf: ViewContainerRef,
        private ryber: RyberService
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
