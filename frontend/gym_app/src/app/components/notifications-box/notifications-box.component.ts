import { Component } from '@angular/core';

@Component({
  selector: 'app-notifications-box',
  template: `
<div class="card">
  <div class="card-header">Notification</div>
  <div class="card-body">
    <div class="d-flex align-items-center">
      <div class="m-2"><i class="fa-solid fa-bell"></i></div>
      <div class="flex-grow-1">Pop-up Notification</div>
      <div class="form-check form-switch">
        <input class="form-check-input" type="checkbox" id="toggleSwitch">
      </div>
    </div>
  </div>
</div>
  `,
  styles: [`.card {
    border: none;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  .card-header {
    background-color: #80ADCA;}`],
})
export class NotificationsBoxComponent {}
