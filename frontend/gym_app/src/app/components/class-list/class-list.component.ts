import { Component, OnInit } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';

@Component({
  selector: 'app-class-list',
  templateUrl: './class-list.component.html',
  styleUrls: ['./class-list.component.css']
})
export class ClassListComponent implements OnInit {

  classes: any[] | undefined;

  constructor(private userService: UsuariosService) {}

  ngOnInit() {
    this.userService.getClasses().subscribe({
      next: (classes: any) => {
        this.classes = classes;
        console.log(this.classes);
      },
      error: (error) => {
        alert('Error al obtener las clases');
      },
      complete: () => {
        console.log('Finalizó');
      }
    });
  }
}
