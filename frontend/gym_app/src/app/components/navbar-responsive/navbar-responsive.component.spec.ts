import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NavbarResponsiveComponent } from './navbar-responsive.component';

describe('NavbarResponsiveComponent', () => {
  let component: NavbarResponsiveComponent;
  let fixture: ComponentFixture<NavbarResponsiveComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [NavbarResponsiveComponent]
    });
    fixture = TestBed.createComponent(NavbarResponsiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
