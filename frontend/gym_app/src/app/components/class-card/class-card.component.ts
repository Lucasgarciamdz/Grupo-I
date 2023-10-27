import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-class-card',
  templateUrl: './class-card.component.html',
  styleUrls: ['./class-card.component.css']
})
export class ClassCardComponent {
  @Input()
  title!: string;
  @Input() 
  items!: { image: string, title: string, description: string, buttonText: string }[];
}
