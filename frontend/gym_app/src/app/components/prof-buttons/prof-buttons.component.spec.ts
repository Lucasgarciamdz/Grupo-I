import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfButtonsComponent } from './prof-buttons.component';

describe('ProfButtonsComponent', () => {
  let component: ProfButtonsComponent;
  let fixture: ComponentFixture<ProfButtonsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProfButtonsComponent]
    });
    fixture = TestBed.createComponent(ProfButtonsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
