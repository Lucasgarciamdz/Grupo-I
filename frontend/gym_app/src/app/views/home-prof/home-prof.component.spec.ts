import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HomeProfComponent } from './home-prof.component';

describe('HomeProfComponent', () => {
  let component: HomeProfComponent;
  let fixture: ComponentFixture<HomeProfComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [HomeProfComponent]
    });
    fixture = TestBed.createComponent(HomeProfComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
