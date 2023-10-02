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
import { UserListComponent } from './components/user-list/user-list.component';
import { ClassListComponent } from './components/class-list/class-list.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'signup', component: SignupComponent},
  { path: 'signin', component: SigninComponent},
  { path: 'profile', component: ProfileComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor', 'Alumno', 'Admin'] } },
  { path: 'edit-profile', component: EditProfileComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor', 'Alumno', 'Admin'] } },
  { path: 'home-prof', component: HomeProfComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor'] } },
  { path: 'stud-work', component: StudWorkComponent, canActivate: [AuthsessionGuard], data: { roles: ['Alumno'] } },
  { path: 'home-admin', component: HomeAdminComponent, canActivate: [AuthsessionGuard], data: { roles: ['Admin'] }},
  { path: 'user-list', component: UserListComponent},
  { path: 'class-list', component: ClassListComponent},
  { path: 'prof-buttons', component: ProfButtonsComponent, canActivate: [AuthsessionGuard], data: { roles: ['Profesor'] } },
  { path: 'admin-buttons', component: ProfButtonsComponent, canActivate: [AuthsessionGuard], data: { roles: ['Admin'] } },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: '**', redirectTo: '/home' },
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule { }