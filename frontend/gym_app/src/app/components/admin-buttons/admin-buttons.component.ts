import { Component } from '@angular/core';

@Component({
  selector: 'app-admin-buttons',
  templateUrl: './admin-buttons.component.html',
  styleUrls: ['./admin-buttons.component.css']
})
export class AdminButtonsComponent {
  students: string[] = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5', 'Student 6'];
  classes: string[] = ['Class A', 'Class B', 'Class C', 'Class D', 'Class E', 'Class F'];
}

