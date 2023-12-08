import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfesorCheckComponent } from './profesor-check.component';

describe('ProfesorCheckComponent', () => {
  let component: ProfesorCheckComponent;
  let fixture: ComponentFixture<ProfesorCheckComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProfesorCheckComponent]
    });
    fixture = TestBed.createComponent(ProfesorCheckComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
