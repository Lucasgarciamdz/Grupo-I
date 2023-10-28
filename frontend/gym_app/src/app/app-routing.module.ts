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
import { HomeAdminComponent } from './views/home-admin/home-admin.component';
import { UserListViewComponent } from './views/user-list-view/user-list-view.component';
import { ClassListViewComponent } from './views/class-list-view/class-list-view.component';
import { AlumnoClaseGuard } from './guards/alumnoclase.guard';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'signup', component: SignupComponent},
  { path: 'signin', component: SigninComponent},
  { path: 'profile', component: ProfileComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor', 'Alumno', 'Admin'] } },
  { path: 'profile/:id', component: ProfileComponent, canActivate: [AlumnoClaseGuard], data: { roles: ['Profesor', 'Admin'] }},
  { path: 'edit-profile', component: EditProfileComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor', 'Alumno', 'Admin'] } },
  { path: 'home-prof', component: HomeProfComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor'] } },
  { path: 'stud-work', component: StudWorkComponent, canActivate: [AuthsessionGuard], data: { roles: ['Alumno'] } },
  { path: 'home-admin', component: HomeAdminComponent, canActivate: [AuthsessionGuard], data: { roles: ['admin', 'Profesor'] }},
  { path: 'user-list-view', component: UserListViewComponent},
  { path: 'class-list-view', component: ClassListViewComponent},
  { path: 'prof-buttons', component: ProfButtonsComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor'] } },
  { path: 'admin-buttons', component: ProfButtonsComponent, canActivate: [AuthsessionGuard], data: { roles: ['admin', 'Profesor'] } },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: '**', redirectTo: '/home' },
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule { }