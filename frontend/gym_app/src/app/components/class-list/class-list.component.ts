import { Component } from '@angular/core';

@Component({
  selector: 'app-class-list',
  templateUrl: './class-list.component.html',
  styleUrls: ['./class-list.component.css']
})
export class ClassListComponent {
  classes = [
    { name: 'Class A', studentCount: 25, instructor: 'Instructor A' },
    { name: 'Class B', studentCount: 20, instructor: 'Instructor B' },
    { name: 'Class C', studentCount: 30, instructor: 'Instructor C' },
    // ... other classes
  ];

  editClass(classInfo: any) {
    // Implement logic to edit class here
    alert('Edit class functionality will be implemented soon!');
  }

  deleteClass(classInfo: any) {
    // Implement logic to delete class here
    alert('Delete class functionality will be implemented soon!');
  }
}
