import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NotificationsBoxComponent } from './notifications-box.component';

describe('NotificationsBoxComponent', () => {
  let component: NotificationsBoxComponent;
  let fixture: ComponentFixture<NotificationsBoxComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [NotificationsBoxComponent]
    });
    fixture = TestBed.createComponent(NotificationsBoxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
