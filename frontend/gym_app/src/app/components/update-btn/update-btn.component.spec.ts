import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateBtnComponent } from './update-btn.component';

describe('UpdateBtnComponent', () => {
  let component: UpdateBtnComponent;
  let fixture: ComponentFixture<UpdateBtnComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UpdateBtnComponent]
    });
    fixture = TestBed.createComponent(UpdateBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
