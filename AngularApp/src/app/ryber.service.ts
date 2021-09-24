import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { of } from 'rxjs';
import { delay,tap } from 'rxjs/operators';

@Injectable({
    providedIn: 'root'
})
export class RyberService {

    constructor(
        public router: Router,
        public http: HttpClient
    ) { }

    store = {
        meta:{
            items:["111-222-3333","email@gmail.com","567 ABC Road, Wakanda"]
            .map((x:any,i)=>{
                return {
                    text:x
                }
            })
        },
        categories:{
            items:["Hot deals","QR Codes","NFT's","T-shirts"]
            .map((x:any,i)=>{
                return {
                    text:x
                }
            })
        },
        info:{
            items:["About","Contact","Privacy Policy","Orders/Returns","Terms & Conditions"]
            .map((x:any,i)=>{
                return {
                    text:x
                }
            })
        },
        service:{
            items:["My account","View Cart","Wishlist","Track My Order","Help"]
            .map((x:any,i)=>{
                return {
                    text:x
                }
            })
        }
    }
}
