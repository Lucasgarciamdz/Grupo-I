import { Component, OnInit } from '@angular/core';
import { ClasesService } from 'src/app/services/clases.service';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit{
  searchText = '';
  classes: any[] = [];
  filteredClasses: any[] = [];

  constructor(private clasesService: ClasesService) { }

  ngOnInit() {
    this.clasesService.getClases().subscribe({
      next: (response: any[]) => {
        this.classes = response;
      },
      error: (error) => {
        console.error(error);
      },
    });
  }

  filterClasses() {
    this.filteredClasses = this.classes.filter(clase => clase.description.includes(this.searchText));
  }
}