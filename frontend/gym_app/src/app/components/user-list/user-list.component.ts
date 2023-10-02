import { Component } from '@angular/core';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent {
  users = [
    { name: 'User 1', role: 'Alumno', status: 'Activo' },
    { name: 'User 2', role: 'Alumno', status: 'Activo' },
    { name: 'User 3', role: 'Alumno', status: 'Inactivo' },
    // ... other users
  ];

  editUser(user: any) {
    // Implement logic to edit user here
    alert('Edit user functionality will be implemented soon!');
  }

  deleteUser(user: any) {
    // Implement logic to delete user here
    alert('Delete user functionality will be implemented soon!');
  }
}
