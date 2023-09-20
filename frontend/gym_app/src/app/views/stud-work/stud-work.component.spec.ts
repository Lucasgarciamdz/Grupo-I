import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StudWorkComponent } from './stud-work.component';

describe('StudWorkComponent', () => {
  let component: StudWorkComponent;
  let fixture: ComponentFixture<StudWorkComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [StudWorkComponent]
    });
    fixture = TestBed.createComponent(StudWorkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
