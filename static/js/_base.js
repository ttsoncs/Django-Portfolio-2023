import { annotate, annotationGroup } from 'https://unpkg.com/rough-notation?module'

const e1 = document.querySelector('#n1')
const e2 = document.querySelector('#n2')
const e3 = document.querySelector('#n3')
const e4 = document.querySelector('#n4')
const e5 = document.querySelector('#n5')

const a1 = annotate(e1, { type: 'underline', color: '#FF218C', strokeWidth: '1.5', padding: -1})
const a2 = annotate(e2, { type: 'box', color: '#FFD800', strokeWidth: '1.5' })
const a3 = annotate(e3, { type: 'box', color: '#21B1FF', strokeWidth: '1.5' })
const a4 = annotate(e4, { type: 'box', color: '#38ef7d', strokeWidth: '1.5' })
const a5 = annotate(e5, { type: 'underline', color: '#9c9c9c', strokeWidth: '1', iterations: 1, animate: false, padding: -5 }) 

const ag = annotationGroup([a1, a2, a3, a4]);
ag.show();

a5.show();

