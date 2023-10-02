import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './views/home/home.component';
import { ProfileComponent } from './views/profile/profile.component';
import { SigninComponent } from './views/signin/signin.component';
import { SignupComponent } from './views/signup/signup.component';
import { EditProfileComponent } from './views/edit-profile/edit-profile.component';
import { HomeProfComponent } from './views/home-prof/home-prof.component';
import { StudWorkComponent } from './views/stud-work/stud-work.component';
import { ProfButtonsComponent } from './components/prof-buttons/prof-buttons.component';
import { AuthsessionGuard } from './guards/authsession.guard';


const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'signup', component: SignupComponent},
  { path: 'signin', component: SigninComponent},
  { path: 'profile', component: ProfileComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor', 'Alumno'] } },
  { path: 'edit-profile', component: EditProfileComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor', 'Alumno'] } },
  { path: 'home-prof', component: HomeProfComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor'] } },
  { path: 'stud-work', component: StudWorkComponent, canActivate: [AuthsessionGuard], data: { roles: ['Alumno'] } },
  { path: 'prof-buttons', component: ProfButtonsComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor'] } },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: '**', redirectTo: '/home' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule { }