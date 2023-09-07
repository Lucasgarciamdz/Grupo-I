import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ResponsiveWorkoutsCardsComponent } from './responsive-workouts-cards/responsive-workouts-cards.component';
import { HomeComponent } from './home/home.component';
import { NavbarComponent } from './navbar/navbar.component';
import { NavbarResponsiveComponent } from './navbar-responsive/navbar-responsive.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { ListaPlanificacionesComponent } from './lista-planificaciones/lista-planificaciones.component';
import { PlanificacionesComponent } from './planificaciones/planificaciones.component';

@NgModule({
  declarations: [
    AppComponent,
    ResponsiveWorkoutsCardsComponent,
    HomeComponent,
    NavbarComponent,
    NavbarResponsiveComponent,
    SearchBarComponent,
    ListaPlanificacionesComponent,
    PlanificacionesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
