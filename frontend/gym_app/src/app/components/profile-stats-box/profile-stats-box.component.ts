import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-profile-stats-box',
  template: `
<div class="card">
  <div class="card-body">
    <div class="d-flex flex-column align-items-center">
      <div class="text-primary">{{ number }}</div>
      <div class="text-muted">{{ label }}</div>
    </div>
  </div>
</div>
  `,
  styles: [
    `
    .card {
  border: none;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.card-body {
  padding: 20px;
}

.text-primary {
  font-size: 24px;
  font-weight: bold;
  color: #007bff;
}

.text-muted {
  font-size: 14px;
  color: #6c757d;
}
    `
  ],
})
export class ProfileStatsBoxComponent {
  @Input() number: string = '180cm';
  @Input() label: string = 'Height';
}
