import { Component } from '@angular/core';

@Component({
  selector: 'app-edit-profile-btn',
  template: `
            <button class="btn btn-primary rounded-circle" routerLink="/edit-profile">
              <i class="fas fa-edit"></i>
            </button>
              `,
  styles: [
  ]
})
export class EditProfileBtnComponent {

}
