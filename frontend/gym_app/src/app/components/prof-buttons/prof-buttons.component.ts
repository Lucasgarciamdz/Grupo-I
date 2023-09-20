import { Component } from '@angular/core';

@Component({
  selector: 'app-prof-buttons',
  templateUrl: './prof-buttons.component.html',
  styleUrls: ['./prof-buttons.component.css']
})
export class ProfButtonsComponent {
  students: string[] = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5', 'Student 6'];
  classes: string[] = ['Class A', 'Class B', 'Class C', 'Class D', 'Class E', 'Class F'];
}
