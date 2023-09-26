import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';

@Component({
  selector: 'app-update-btn',
  templateUrl: './update-btn.component.html',
  styleUrls: ['./update-btn.component.css']
})
export class UpdateBtnComponent implements OnInit {
  previousUrl: string = '';

  constructor(private router: Router) {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        this.previousUrl = this.router.url;
      }
    });
  }

  ngOnInit() {}

  redirigir() {
    // Utiliza this.previousUrl para redirigir según la URL anterior
    if (this.previousUrl === '/profile') {
      this.router.navigate(['/profile']);
    } else if (this.previousUrl === '/profile-prof') {
      this.router.navigate(['/profile-prof']);
    }
  }
}
