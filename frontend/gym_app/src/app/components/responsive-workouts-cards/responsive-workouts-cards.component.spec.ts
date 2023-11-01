import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResponsiveWorkoutsCardsComponent } from './responsive-workouts-cards.component';

describe('ResponsiveWorkoutsCardsComponent', () => {
  let component: ResponsiveWorkoutsCardsComponent;
  let fixture: ComponentFixture<ResponsiveWorkoutsCardsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ResponsiveWorkoutsCardsComponent]
    });
    fixture = TestBed.createComponent(ResponsiveWorkoutsCardsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});