import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlanificacionesViewComponent } from './planificaciones-view.component';

describe('PlanificacionesViewComponent', () => {
  let component: PlanificacionesViewComponent;
  let fixture: ComponentFixture<PlanificacionesViewComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PlanificacionesViewComponent]
    });
    fixture = TestBed.createComponent(PlanificacionesViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
