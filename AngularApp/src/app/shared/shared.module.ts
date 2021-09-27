import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SharedRoutingModule } from './shared-routing.module';
import { MediaPrefixPipe } from '../media-prefix.pipe';
import { SanitizedComponent } from './sanitized/sanitized.component';
import { SanitizeUrlPipe } from '../sanitize-url.pipe';
import { NavComponent } from './nav/nav.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';


@NgModule({
  declarations: [
    MediaPrefixPipe,

    SanitizedComponent,
    SanitizeUrlPipe,
    NavComponent,
    HeaderComponent,
    FooterComponent,
  ],
  imports: [
    CommonModule,
    SharedRoutingModule
  ],
  exports: [
    MediaPrefixPipe,

    SanitizedComponent,
    SanitizeUrlPipe,
    NavComponent,
    HeaderComponent,
    FooterComponent,
  ]
})
export class SharedModule { }
