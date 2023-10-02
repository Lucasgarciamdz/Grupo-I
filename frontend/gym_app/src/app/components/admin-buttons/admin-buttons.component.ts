import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-admin-buttons',
  templateUrl: './admin-buttons.component.html',
  styleUrls: ['./admin-buttons.component.css']
})
export class AdminButtonsComponent {
  constructor(private router: Router) {}

  showUserList() {
    this.router.navigate(['/user-list']);
  }

  showClassList() {
    this.router.navigate(['/class-list']);
  }
}
