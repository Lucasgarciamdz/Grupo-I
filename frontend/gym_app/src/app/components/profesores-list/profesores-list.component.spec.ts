import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfesoresListComponent } from './profesores-list.component';

describe('ProfesoresListComponent', () => {
  let component: ProfesoresListComponent;
  let fixture: ComponentFixture<ProfesoresListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProfesoresListComponent]
    });
    fixture = TestBed.createComponent(ProfesoresListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
