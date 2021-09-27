import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CreateAcctRoutingModule } from './create-acct-routing.module';
import { MainComponent } from './main/main.component';


@NgModule({
  declarations: [
    MainComponent
  ],
  imports: [
    CommonModule,
    CreateAcctRoutingModule
  ],
  exports: [
    MainComponent
  ]
})
export class CreateAcctModule { }
