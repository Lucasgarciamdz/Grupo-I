import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ResponsiveWorkoutsCardsComponent } from './components/responsive-workouts-cards/responsive-workouts-cards.component';
import { HomeComponent } from './views/home/home.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { NavbarResponsiveComponent } from './components/navbar-responsive/navbar-responsive.component';
import { SearchBarComponent } from './components/search-bar/search-bar.component';
import { ListaPlanificacionesComponent } from './components/lista-planificaciones/lista-planificaciones.component';
import { PlanificacionesComponent } from './components/planificaciones/planificaciones.component';
import { ProfilePictureComponent } from './components/profile-picture/profile-picture.component';
import { ProfileComponent } from './views/profile/profile.component';
import { AccountInfoComponent } from './components/account-info/account-info.component';
import { NotificationsBoxComponent } from './components/notifications-box/notifications-box.component';
import { ProfileStatsBoxComponent } from './components/profile-stats-box/profile-stats-box.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { SigninComponent } from './views/signin/signin.component';
import { SignupComponent } from './views/signup/signup.component';
import { ProfButtonsComponent } from './components/prof-buttons/prof-buttons.component';
import { TitleComponent } from './components/title/title.component';

@NgModule({
  declarations: [
    AppComponent,
    ResponsiveWorkoutsCardsComponent,
    HomeComponent,
    NavbarComponent,
    NavbarResponsiveComponent,
    SearchBarComponent,
    ListaPlanificacionesComponent,
    PlanificacionesComponent,
    ProfilePictureComponent,
    ProfileComponent,
    AccountInfoComponent,
    NotificationsBoxComponent,
    ProfileStatsBoxComponent,
    SignUpComponent,
    SigninComponent,
    SignupComponent,
    ProfButtonsComponent,
    TitleComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
