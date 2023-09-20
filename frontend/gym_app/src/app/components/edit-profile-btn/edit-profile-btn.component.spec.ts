import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditProfileBtnComponent } from './edit-profile-btn.component';

describe('EditProfileBtnComponent', () => {
  let component: EditProfileBtnComponent;
  let fixture: ComponentFixture<EditProfileBtnComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EditProfileBtnComponent]
    });
    fixture = TestBed.createComponent(EditProfileBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
