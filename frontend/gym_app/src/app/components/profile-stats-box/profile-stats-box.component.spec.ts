import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfileStatsBoxComponent } from './profile-stats-box.component';

describe('ProfileStatsBoxComponent', () => {
  let component: ProfileStatsBoxComponent;
  let fixture: ComponentFixture<ProfileStatsBoxComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProfileStatsBoxComponent]
    });
    fixture = TestBed.createComponent(ProfileStatsBoxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
