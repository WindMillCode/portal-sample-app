import { Optional } from "@angular/core"

export  function mediaPrefix(devObj){
    let {media} = devObj
    return "./assets/media/"+media
}

export function numberParse(   devObj:any  ){
    // string or array
    let {dim} = devObj
    if(typeof dim === "string"){
        return parseFloat(dim.split("p")[0])
    }
    else{
        return dim
        .map((x:any,i)=>{
            return parseFloat(x.split("p")[0])
        })
    }
}

export function classPrefix(devObj:{view:string}){
    let {view} = devObj
    let prefix = "a_p_p_"+view
    return (devObj:{val:string})=>{
        let {val} = devObj
        return prefix+val
    }
}

export function eventDispatcher(   devObj:{event:string,element:HTMLElement | Window | Element}   ){

    try {
        let event0= new Event(devObj.event)
        devObj.element.dispatchEvent(event0)
        // console.log(event0)
    }
    catch(e){
        let eventLegacy = document.createEvent("Event");
        eventLegacy.initEvent(devObj.event, false, true);
        devObj.element.dispatchEvent(eventLegacy)
    }
}


export class LinkedList{

    constructor(startVal:any){
        this._head.val = startVal;
        (this.list as any) = this._head
    }

    addNode= (devObj)=>{
        let {val} = devObj
        ;(this.list as any).next = {
            val,
            next:null
        }
        this.list =  (this.list as any).next
    }

    head= ()=>{
        return this._head
    }



    _head= {
        val:null,
        next:null
    }

    list= null
}

type RequireOnlyOne<T, Keys extends keyof T = keyof T> =
    Pick<T, Exclude<keyof T, Keys>>
    & {
        [K in Keys]-?:
            Required<Pick<T, K>>
            & Partial<Record<Exclude<Keys, K>, undefined>>
    }[Keys]

type SamePropTypeOnly<T> = {
    [P: string]: T;
}

// dev additions

// types
export function accountMetadata(){
    return Object.fromEntries(
        ["First Name","Last Name","Email","Phone","Address","City","State","Zip Code","Country"]
        .map((x:any,i)=>{
            return [x.toLowerCase().split(" ").join("_"),""]
        })
    )
}
export type cartCreate = {
    message:{
        cartId:string
    }
}
export type Account ={
    user:string,
    pass:string
    billing:{
        items: { [k: string]: {
            placeholder: string;
            value: string;
            blur: (evt:Event |any) => void; };
        }
    },
    shipping:{
        sameAsBilling:{
            checked:boolean,
        },
        info:{
            items:{ [k: string]: {
                placeholder: string;
                value: string;
                blur: (evt:Event |any) => void; };
            }
        }
    },
}

export type RyberProductsItems ={
    title:{
        text:string
    },
    img:{
        src:string
    },
    price:{
        text: string , //`$${number}`
        value:number
    },
    addItem:{
        click:(evt:MouseEvent) => void,
        inCart:boolean
    },
    removeItem:{
        click:(evt:MouseEvent) => void,
    },
    quantity:{
        input:{
            value:number,
            blur: (evt:FocusEvent|any) => void;
            focusout: (evt:FocusEvent|any) => void;
        },
        add:{
            click:(evt:MouseEvent) => void,
        },
        remove:{
            click:(evt:MouseEvent) => void,
        }
    },
    subtotal:{
        text:()=>string,
        value:()=>number
    }
}
export  type RyberStore = {
    [key:string]:any,
    accounts:{
        [key:string]:any,
        all:{
            items:Array<Account>
        },
        current:Partial<Account>,
        logout:{
            click:(MouseEvent)=> void
        },
        ui:{
            items:Array<{
                placeholder:string,
                value:string,
                blur:(evt:FocusEvent)=>void,
                focusout:(evt:FocusEvent)=>void
            }>
        }
    },
    checkout:{
        billing:{
            items: { [k: string]: {
                placeholder: string;
                value: string;
                blur: (evt:Event |any) => void; };
            }
        },
        shipping:{
            sameAsBilling:{
                checked:boolean,
                change: (evt:Event |any) => void;
            },
            info:{
                items:{ [k: string]: {
                    placeholder: string;
                    value: string;
                    blur: (evt:Event |any) => void; };
                }
            }
        },
        payment:{
            paypal:{
                option:{
                    checked:boolean,
                    change: (evt:Event |any) => void;
                }
            },
            placeOrder:{
                click: (evt:Event |any) => void;
            }
        }
    },
    cart:{
        empty:boolean,
        items:Array<any>,
        total:{
            value:()=>number,
            text:()=>string
        },
        id:string
    },
    products:{
        items:Array<RyberProductsItems>
    }
}

// dev dummy additions
export let populateProducts = (devObj)=>{
    let {ryber,ref,iif,env,tap} = devObj
    ryber.store.products.items =Array(7).fill(null)
    .map((x:string,i)=>{
        let result:RyberProductsItems ={
            title:{
                text:["QR Code 1","QR Code 2","NFT 1", "NFT 2","T-shirt 1","T shirt 2","T -shirt 3"][i]
            },
            img:{
                src:[
                    mediaPrefix({media:'shop_1.png'}),
                    mediaPrefix({media:'shop_1.png'}),
                    mediaPrefix({media:'shop_0.jpg'}),
                    mediaPrefix({media:'shop_0.jpg'}),
                    mediaPrefix({media:'shop_2.jpg'}),
                    mediaPrefix({media:'shop_3.jpg'}),
                    mediaPrefix({media:'shop_4.jpg'}),
                ][i]
            },
            price:{
                text:["$29.99","$29.99","$54.99","$54.99","$22.99","$25.99","$22.99"][i],
                value:[29.99,29.99,54.99,54.99,22.99,25.99,22.99][i]
            },
            addItem:{
                click:(evt:MouseEvent)=>{

                    if(!result.addItem.inCart){
                        ryber.store.cart.items.push(result)
                        ryber.router.navigateByUrl('/cart');
                        result.addItem.inCart = true
                    }
                    else{
                        result.quantity.input.value += 1
                        ryber.router.navigateByUrl('/cart');
                    }

                    // XHR to add item to cart
                        // there must be user
                    if(ryber.store.accounts.current.user){
                        // create or update cart depending on present id
                        iif(
                            ()=>{return ryber.store.cart.id === ""},
                            ryber.http.put(
                                `${env.backend.url}/cart/create`,
                                {
                                    cartData:{
                                        cart:ryber.store.cart.items
                                        .map((x:any,i)=>{
                                            return {
                                                img:x.img,
                                                price:x.price,
                                                quantity:{
                                                    input:x.quantity.input
                                                },
                                                title:x.title
                                            }
                                        }),
                                        total:ryber.store.cart.total.value(),
                                    },
                                    userData:{
                                        user:ryber.store.accounts.current.user,
                                        pass:ryber.store.accounts.current.pass
                                    }
                                }
                            ),
                            ryber.http.patch(
                                `${env.backend.url}/cart/update`,
                                {
                                    data:{
                                        cart_id:ryber.store.cart.id,
                                        update_body:{
                                            cart:ryber.store.cart.items
                                            .map((x:any,i)=>{
                                                return {
                                                    img:x.img,
                                                    price:x.price,
                                                    quantity:{
                                                        input:x.quantity.input
                                                    },
                                                    title:x.title
                                                }
                                            }),
                                            total:ryber.store.cart.total.value(),
                                        }
                                    }
                                }
                            )
                        )
                        .pipe(
                            tap((result:any |any)=>{
                                if(ryber.store.cart.id === ""){
                                    ryber.store.cart.id = result.message.cartId
                                }
                            },console.error),
                        )
                        .subscribe()

                    }
                    //

                },
                inCart:false
            },
            removeItem:{
                click:(evt:MouseEvent)=>{
                    let index = ryber.store.cart.items.indexOf(result)
                    ryber.store.cart.items.splice(index,1)
                    result.addItem.inCart = false
                }
            },
            quantity:{
                input:{
                    value:1,
                    blur:(evt:FocusEvent |any)=>{
                        result.quantity.input.value = evt.target.value
                    },
                    focusout:(evt:FocusEvent |any)=>{
                        result.quantity.input.value = evt.target.value
                    }
                },
                add:{
                    click:(evt:MouseEvent)=>{
                        result.quantity.input.value++
                    }
                },
                remove:{
                    click:(evt:MouseEvent)=>{
                        if(result.quantity.input.value>1){
                            result.quantity.input.value--
                        }
                    }
                }
            },
            subtotal:{
                text:()=>{
                    return "$"+result.subtotal.value()
                },
                value:()=>{
                    let value = (result.price.value*result.quantity.input.value).toFixed(2)
                    return parseFloat(value)
                }
            }
        }
        return result
    })
ref.detectChanges()
}
