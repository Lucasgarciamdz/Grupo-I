import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClasesListComponent } from './clases-list.component';

describe('ClasesListComponent', () => {
  let component: ClasesListComponent;
  let fixture: ComponentFixture<ClasesListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ClasesListComponent]
    });
    fixture = TestBed.createComponent(ClasesListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
