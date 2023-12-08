import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfCheckViewComponent } from './prof-check-view.component';

describe('ProfCheckViewComponent', () => {
  let component: ProfCheckViewComponent;
  let fixture: ComponentFixture<ProfCheckViewComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProfCheckViewComponent]
    });
    fixture = TestBed.createComponent(ProfCheckViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
