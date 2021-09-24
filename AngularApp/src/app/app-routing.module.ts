import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router'; // CLI imports router

const routes: Routes = [

    {
        path:'home',
        loadChildren: () => import('./home/home.module').then(m => m.HomeModule)
    },
    {
        path:'shop',
        loadChildren: () => import('./shop/shop.module').then(m => m.StoreModule)
    },
    {
        path:'cart',
        loadChildren: () => import('./cart/cart.module').then(m => m.CartModule)
    },
    {
        path: '',
        loadChildren: () => import('./home/home.module').then(m => m.HomeModule)
      }
]; // sets up routes constant where you define your routes

// configures NgModule imports and exports
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
