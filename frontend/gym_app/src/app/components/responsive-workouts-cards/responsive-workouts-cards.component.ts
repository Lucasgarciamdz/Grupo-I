import { Component, Input, OnInit } from '@angular/core';
import { ClasesService } from '../../services/clases.service';
import { JWTService } from '../../services/jwt.service';

@Component({
  selector: 'app-responsive-workouts-cards',
  templateUrl: './responsive-workouts-cards.component.html',
  styleUrls: ['./responsive-workouts-cards.component.css']
})
export class ResponsiveWorkoutsCardsComponent implements OnInit {
  @Input() title!: string;
  @Input() items: any[] = []; // Mantenemos el nombre "items" para mantener la consistencia

  constructor(private clasesService: ClasesService, private jwtService: JWTService) {}

  ngOnInit() {
    const userId = this.jwtService.getId(); // Obtener el ID del usuario que inició sesión

    if (userId) {
      // Utiliza el servicio para obtener las clases asociadas al usuario
      const userIdAsNumber = parseInt(userId, 10);
      this.clasesService.getClasesByAlumno(userIdAsNumber).subscribe((data: any) => {
        this.items = data; // Asigna los datos de las clases asociadas a la propiedad items
      });
    }
  }
}
