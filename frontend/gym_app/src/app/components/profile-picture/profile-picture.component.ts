import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-profile-picture',
  template: `
    <img [src]="image" class="img img-thumbnail rounded-circle mx-auto d-block" alt="Profile Picture">
    <h2 class="text-center">{{ name || "alumno x"}}</h2>
  `,
  styles: [
    `
    img {
      max-width: 25%;
      max-height: 25%;
    }
    `
  ]
})
export class ProfilePictureComponent {
  @Input() image: string | undefined;
  @Input() name: string | undefined;
}