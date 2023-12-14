import { Component } from '@angular/core';

@Component({
  selector: 'app-edit-profile-btn',
  template: `
            <button class="btn rounded-circle" routerLink="/edit-profile">
              <i class="fas fa-edit"></i>
            </button>
              `,
  styles: [
    `
    .btn {
      color: #3A6A87;
      height: 24px;
      width: 24px;
      padding-bottom: 48px;
}

    `
  ]
})
export class EditProfileBtnComponent {

}
